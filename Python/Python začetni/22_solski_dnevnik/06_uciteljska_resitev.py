# Učiteljska referenčna rešitev – 22 Mini šolski dnevnik

dnevnik = {
    "Ana": {"razred": 7, "matematika": 4, "anglescina": 5, "sport": 5},
    "Klara": {"razred": 7, "matematika": 3, "anglescina": 3, "sport": 5},
    "Luka": {"razred": 8, "matematika": 5, "anglescina": 5, "sport": 4},
}


def izpisi_ucenca(ime):
    if ime not in dnevnik:
        print("Tega učenca ni v dnevniku.")
        return

    podatki = dnevnik[ime]
    print(f"Učenec: {ime}")
    print(f"Razred: {podatki['razred']}")
    for predmet, ocena in podatki.items():
        if predmet != 'razred':
            print(f"- {predmet}: {ocena}")


def povprecje_ucenca(ime):
    podatki = dnevnik[ime]
    ocene = []
    for predmet, ocena in podatki.items():
        if predmet != 'razred':
            ocene.append(ocena)
    return sum(ocene) / len(ocene)

for ime in dnevnik:
    print(f"{ime}: povprečje = {povprecje_ucenca(ime):.2f}")
