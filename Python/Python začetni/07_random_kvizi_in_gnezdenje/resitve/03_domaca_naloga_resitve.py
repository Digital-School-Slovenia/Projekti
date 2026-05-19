"""Rešitve domače naloge – 07 – Random, mini kvizi in odločanje v praksi."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

import random

random.seed(11)

vprasanja = [
    ("Koliko je 3 + 4?", "7"),
    ("Katero mesto je glavno mesto Slovenije?", "Ljubljana"),
]

tocke = 0
for besedilo, pravilen_odgovor in vprasanja:
    izbran_namig = random.choice(["Premisli mirno.", "Preveri osnovno dejstvo."])
    odgovor = pravilen_odgovor
    print(besedilo)
    print(f"Namig: {izbran_namig}")
    if odgovor.lower() == pravilen_odgovor.lower():
        tocke += 1

print(f"\nSkupni rezultat: {tocke}/{len(vprasanja)}")
print("Pri gnezdenju je pomembno, da se drugo vprasanje izvede v pravem delu programa.")
