"""Resitve domace naloge - 28 Projekt Mini Zelda."""


def dodaj_nadgradnjo(stanje):
    stanje["mana"] = 3
    stanje["poseben_napad"] = True
    return stanje


razlaga_kode = {
    "kamera": "kamera sledi igralcu tako, da se svet izrisuje glede na odmik kamere",
    "pobiranje_kovancev": "pri vsakem kovancu preverimo trk z igralcem in ob zadetku povecamo score",
    "napad": "napad ustvari mec ali izstrelek pred igralcem in preveri trk s sovraznikom",
}

opis_igre = [
    "Cilj igre je priti do portala in zbrati dovolj tock.",
    "Igralec je junak, ki se premika po zemljevidu.",
    "Sovrazniki so posasti, ki odstevajo zivljenja.",
    "Zmaga je, ko dosezes cilj, poraz pa, ko zmanjka zivljenj.",
]

stanje = {"hp": 4, "score": 9}
print(dodaj_nadgradnjo(stanje))
for podrocje, razlaga in razlaga_kode.items():
    print(f"{podrocje}: {razlaga}")
for vrstica in opis_igre:
    print(vrstica)
