"""Resitve domace naloge - 35 Zakljucni projekt."""

projekt = {
    "vecja_napaka": "Trk se ni pravilno zaznal ob robu zaslona.",
    "nova_nadgradnja": "Dodan je bonus predmet, ki za kratek cas podvoji tocke.",
    "opis": [
        "Projekt je akcijska igra zbiranja predmetov.",
        "Igralec se premika po zaslonu in zbira zvezde.",
        "Sovrazniki zmanjsujejo zivljenja ob trku.",
        "Zmaga je dosezena pri dovolj visokem rezultatu.",
        "Poraz nastopi, ko zmanjka zivljenj.",
    ],
}


def izpisi_opis(projektni_podatki):
    print(projektni_podatki["vecja_napaka"])
    print(projektni_podatki["nova_nadgradnja"])
    for vrstica in projektni_podatki["opis"]:
        print(vrstica)


izpisi_opis(projekt)