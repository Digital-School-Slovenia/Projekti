"""Rešitve domače naloge – 31 – Projekt – Pac-Man labirint."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

nova_mapa = [
    "#########",
    "#P..#...#",
    "#.#.#.#G#",
    "#.......#",
    "#########",
]

opis_upravljanja = {
    "gor": "premik navzgor",
    "dol": "premik navzdol",
    "levo": "premik levo",
    "desno": "premik desno",
}


def test_trka(mreza, x, y):
    return mreza[y][x] == "#"


print(nova_mapa[0])
for tipka, pomen in opis_upravljanja.items():
    print(f"{tipka}: {pomen}")
print(test_trka(nova_mapa, 0, 0))
print("Pri Pacmanu je kljucno, da vsako potezo preverimo proti mrezi labirinta.")
