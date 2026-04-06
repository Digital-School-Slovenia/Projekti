"""Rešitve dodatnih nalog – 32 – Projekt – Mini Wolfenstein."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

mapa = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
]
stanje = {"prikazi_minimapo": True, "ima_kljuc": False, "predmeti": []}
barve_sten = {1: (180, 180, 180), 3: (120, 170, 255), 4: (220, 120, 120)}


def dodaj_cilj(mreza, x, y):
    nova_mreza = [vrstica[:] for vrstica in mreza]
    nova_mreza[y][x] = 2
    return nova_mreza


def preklopi_minimapo(stanje_igre):
    stanje_igre["prikazi_minimapo"] = not stanje_igre["prikazi_minimapo"]
    return stanje_igre["prikazi_minimapo"]


def obrni_z_misko(kot, premik_miske, obcutljivost=0.0035):
    return kot + premik_miske * obcutljivost


def barva_stene(tip_stene):
    return barve_sten.get(tip_stene, (150, 150, 150))


def lahko_odklenes_vrata(stanje_igre):
    return stanje_igre["ima_kljuc"]


def poberi_predmet(stanje_igre, predmet):
    stanje_igre["predmeti"].append(predmet)
    if predmet == "kljuc":
        stanje_igre["ima_kljuc"] = True
    return stanje_igre


print("Naloga 1")
mapa_z_izhodom = dodaj_cilj(mapa, 4, 3)
print(mapa_z_izhodom)

print("\\nNaloga 2")
print(f"Minimapa aktivna: {preklopi_minimapo(stanje)}")
print(f"Minimapa aktivna: {preklopi_minimapo(stanje)}")

print("\\nNaloga 3")
print(f"Nov kot pogleda: {obrni_z_misko(0.0, 24):.3f}")

print("\\nNaloga 4")
print(barva_stene(1))
print(barva_stene(3))
print(barva_stene(4))

print("\\nNaloga 5")
print(f"Lahko odprem vrata brez kljuca: {lahko_odklenes_vrata(stanje)}")
poberi_predmet(stanje, "kljuc")
print(f"Lahko odprem vrata s kljucem: {lahko_odklenes_vrata(stanje)}")

print("\\nNaloga 6")
poberi_predmet(stanje, "medkit")
print(stanje)
