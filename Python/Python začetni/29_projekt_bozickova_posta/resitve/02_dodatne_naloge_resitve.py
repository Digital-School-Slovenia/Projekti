"""Rešitve dodatnih nalog – 29 – Projekt – Božičkova pošta."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

import random

random.seed(29)


def ustvari_predmet(vrsta):
    return {
        "vrsta": vrsta,
        "x": random.randint(0, 500),
        "y": 0,
        "hitrost": random.randint(3, 7),
    }


def ucinek_predmeta(vrsta, score, zivljenja):
    if vrsta == "pismo":
        score += 10
    elif vrsta == "spam":
        zivljenja -= 1
    elif vrsta == "pikapolonica_srece":
        score += 25
    return score, zivljenja


def combo_bonus(combo):
    if combo >= 5:
        return 20
    if combo >= 3:
        return 10
    return 0


def nova_hitrost(osnovna_hitrost, stopnja):
    return osnovna_hitrost + stopnja


print(ustvari_predmet("pismo"))
print(ucinek_predmeta("spam", 40, 3))
print(combo_bonus(4))
print(nova_hitrost(5, 3))
