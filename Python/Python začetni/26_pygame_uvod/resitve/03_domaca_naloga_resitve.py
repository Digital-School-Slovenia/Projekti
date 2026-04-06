"""Resitve domace naloge - 26 Pygame uvod."""

nastavitve_okna = {
    "sirina": 640,
    "visina": 480,
    "ozadje": (30, 30, 60),
}

pravokotnik = {
    "x": 120,
    "y": 150,
    "sirina": 80,
    "visina": 50,
    "barva": (220, 90, 90),
}


def opis_okna(nastavitve):
    return f"Okno {nastavitve['sirina']} x {nastavitve['visina']} z ozadjem {nastavitve['ozadje']}"


print(opis_okna(nastavitve_okna))
print(f"Pravokotnik bo narisan na ({pravokotnik['x']}, {pravokotnik['y']}).")
print("V pygame bi nato ustvaril okno, pobarval ozadje in narisal pravokotnik s temi podatki.")

razmislek = "Najtezji del pri pygame je razumeti glavno zanko in osvezevanje zaslona v vsakem koraku."
print(razmislek)