"""Rešitve dodatnih nalog – 34 – Delavnica iger in priprava na zaključek."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

rezervna_ideja = {
    "naslov": "Lov na zaklad",
    "opis": "Igralec po zemljevidu pobira namige in se izogiba pastem.",
}

glavna_ideja = {
    "minimum": ["premikanje", "tocke", "konec igre"],
    "bonus": ["sovrazniki", "vec nivojev", "meni"],
}

funkcije = [
    "premikanje_igralca()",
    "preveri_trk()",
    "izpisi_hud()",
    "ponastavi_igro()",
]

spremenljivke = ["score", "player_x", "player_y", "speed", "lives"]
ne_dodam_v_prvi_verziji = ["online nacin", "trgovina", "shramba v oblak"]


def elevator_pitch():
    return "To je hitra igra spretnosti, kjer igralec zbira predmete, se izogiba nevarnostim in poskusa doseci cilj pred iztekom casa."


print(rezervna_ideja)
print(glavna_ideja)
print(funkcije)
print(spremenljivke)
print(ne_dodam_v_prvi_verziji)
print(elevator_pitch())
