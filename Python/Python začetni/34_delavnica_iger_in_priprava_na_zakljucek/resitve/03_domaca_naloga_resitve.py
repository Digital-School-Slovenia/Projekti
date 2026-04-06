"""Resitve domace naloge - 34 Delavnica iger in priprava na zakljucek."""

projekt = {
    "naslov": "Vesoljski skok",
    "opis": "Igralec z raketo pobira energijo in se izogiba asteroidom.",
    "cilj": "Zbrati 20 energijskih kristalov.",
    "zmaga": "Dosezen cilj kristalov.",
    "poraz": "Raketa izgubi vsa zivljenja.",
    "prva_verzija": [
        "ustvari okno",
        "dodaj igralca",
        "premikanje igralca",
        "stetje tock in konec igre",
    ],
    "minimum": "Premikanje, zbiranje predmetov in konec igre.",
    "prva_nadgradnja": "Dodam sovraznike in stevec zivljenj.",
}


def izpisi_povzetek(podatki):
    for kljuc, vrednost in podatki.items():
        print(f"{kljuc}: {vrednost}")


def ogrodje_programa():
    print("# minimum: premikanje, zbiranje, konec")
    print("# prva nadgradnja: sovrazniki")
    print("running = True")
    print("while running:")
    print("    pass")


izpisi_povzetek(projekt)
ogrodje_programa()