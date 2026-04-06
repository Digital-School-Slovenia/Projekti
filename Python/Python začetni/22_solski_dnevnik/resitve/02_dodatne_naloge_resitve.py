"""Resitve dodatnih nalog - 22 Solski dnevnik."""

dnevnik = {
    "Ana": {"razred": "8.a", "ocene": {"matematika": 5, "anglescina": 4}},
    "Bor": {"razred": "8.a", "ocene": {"matematika": 3, "anglescina": 5}},
}


def izpisi_ocene(ime):
    if ime in dnevnik:
        return dnevnik[ime]["ocene"]
    return {}


def spremeni_oceno(ime, predmet, nova_ocena):
    if ime in dnevnik:
        dnevnik[ime]["ocene"][predmet] = nova_ocena


def ima_predmet(ime, predmet):
    return ime in dnevnik and predmet in dnevnik[ime]["ocene"]


def povprecje_razreda():
    vse_ocene = []
    for ucenec in dnevnik.values():
        vse_ocene.extend(ucenec["ocene"].values())
    return sum(vse_ocene) / len(vse_ocene)


print(izpisi_ocene("Ana"))
spremeni_oceno("Bor", "matematika", 4)
print(ima_predmet("Ana", "matematika"))
print(f"Povprecje razreda: {povprecje_razreda():.2f}")