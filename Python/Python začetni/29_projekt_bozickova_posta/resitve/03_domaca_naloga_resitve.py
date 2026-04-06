"""Rešitve domače naloge – 29 – Projekt – Božičkova pošta."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

def nova_nadgradnja(stanje):
    stanje["magnet_za_dobra_pisma"] = True
    return stanje


opis_igre = {
    "cilj": "Ujeti dobra pisma in se izogniti slabim.",
    "igralec": "Postar, ki premika sani levo in desno.",
    "sovraznik": "Slaba posta oziroma spam predmeti.",
    "zmaga": "Dosezen dovolj visok rezultat pred iztekom igre.",
}

navodila = [
    "Premikaj se levo in desno.",
    "Ujemi dobra pisma za tocke.",
    "Izogibaj se slabim predmetom.",
    "Pazi na zivljenja in combo.",
]

print(nova_nadgradnja({"score": 0, "zivljenja": 3}))
for kljuc, vrednost in opis_igre.items():
    print(f"{kljuc}: {vrednost}")
for vrstica in navodila:
    print(vrstica)
