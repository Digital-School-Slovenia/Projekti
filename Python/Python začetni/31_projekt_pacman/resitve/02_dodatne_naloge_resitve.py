"""Resitve dodatnih nalog - 31 Projekt Pacman."""

import random

random.seed(31)

labirint = [
    "########",
    "#..G...#",
    "#.#.##.#",
    "#P.....#",
    "########",
]


def je_stena(mreza, x, y):
    return mreza[y][x] == "#"


def pojej_piko(mreza, x, y):
    vrstica = list(mreza[y])
    if vrstica[x] == ".":
        vrstica[x] = " "
    mreza[y] = "".join(vrstica)


def premik(x, y, dx, dy):
    if not je_stena(labirint, x + dx, y + dy):
        return x + dx, y + dy
    return x, y


def nakljucen_korak_duha(x, y):
    for dx, dy in random.sample([(1, 0), (-1, 0), (0, 1), (0, -1)], 4):
        if not je_stena(labirint, x + dx, y + dy):
            return x + dx, y + dy
    return x, y


print(je_stena(labirint, 0, 0))
print(premik(1, 3, 1, 0))
pojej_piko(labirint, 1, 1)
print(labirint[1])
print(nakljucen_korak_duha(3, 1))