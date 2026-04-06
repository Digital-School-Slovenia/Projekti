"""Resitve dodatnih nalog - 33 Projekt Dodge the Meteors."""

import random

random.seed(33)


def ustvari_meteor():
    return {"x": random.randint(0, 500), "y": 0, "hitrost": random.randint(4, 8)}


def premakni_meteor(meteor):
    meteor["y"] += meteor["hitrost"]
    return meteor


def trk(prvi, drugi):
    return abs(prvi["x"] - drugi["x"]) < 30 and abs(prvi["y"] - drugi["y"]) < 30


def uporabi_powerup(tip, stanje):
    if tip == "scit":
        stanje["scit"] = True
    elif tip == "pocisti_vse":
        stanje["meteorji"] = []
    return stanje


def povecaj_tezavnost(hitrost, nivo):
    return hitrost + nivo


meteor = ustvari_meteor()
print(premakni_meteor(meteor))
print(trk({"x": 100, "y": 200}, {"x": 120, "y": 215}))
print(uporabi_powerup("scit", {"scit": False, "meteorji": [1, 2, 3]}))
print(povecaj_tezavnost(5, 3))