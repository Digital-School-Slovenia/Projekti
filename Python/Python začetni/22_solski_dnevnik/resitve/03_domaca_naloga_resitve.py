"""Rešitve domače naloge – 22 – Slovarji v praksi – mini šolski dnevnik."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

dnevnik = {
    "Nina": {"ocene": {"matematika": 5, "slovenscina": 4}},
    "Tim": {"ocene": {"matematika": 3, "slovenscina": 5}},
}


def povprecje_ucenca(ime):
    ocene = list(dnevnik[ime]["ocene"].values())
    return sum(ocene) / len(ocene)


def dodaj_oceno(ime, predmet, ocena):
    dnevnik[ime]["ocene"][predmet] = ocena


def izpisi_predmete(ime):
    for predmet, ocena in dnevnik[ime]["ocene"].items():
        print(f"{predmet}: {ocena}")


print(f"Povprecje Nine: {povprecje_ucenca('Nina'):.2f}")
dodaj_oceno("Tim", "zgodovina", 4)
izpisi_predmete("Tim")
print("Pri dnevniku moram paziti, kako dostopam do ugnezdenih slovarjev.")
