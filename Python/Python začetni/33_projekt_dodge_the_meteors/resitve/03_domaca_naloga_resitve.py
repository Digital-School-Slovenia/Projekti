"""Resitve domace naloge - 33 Projekt Dodge the Meteors."""

def nova_nadgradnja(stanje):
    stanje["dvojne_tocke"] = True
    return stanje


def novo_zacetno_stanje():
    return {"score": 0, "zivljenja": 3, "scit": False, "meteorji": []}


opis_igre = [
    "Igralec se izmika meteorjem.",
    "Za prezivet cas dobi tocke.",
    "Vsak trk odsteje zivljenje.",
    "Power-up lahko za kratek cas vklopi scit.",
    "Igra se konca, ko zmanjka zivljenj.",
]

print(nova_nadgradnja(novo_zacetno_stanje()))
for vrstica in opis_igre:
    print(vrstica)