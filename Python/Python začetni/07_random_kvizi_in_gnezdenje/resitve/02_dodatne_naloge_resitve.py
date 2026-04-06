"""Resitve dodatnih nalog - 07 Random, kvizi in gnezdenje."""

import random

random.seed(7)

def ugibanje(ugib):
    skrito = random.randint(1, 10)
    if ugib == skrito:
        return f"Pravilno. Skrito stevilo je bilo {skrito}."
    return f"Napacno. Skrito stevilo je bilo {skrito}."


def mini_kviz(odgovor_1, odgovor_2):
    tocke = 0
    if odgovor_1.lower() == "pariz":
        tocke += 1
        if odgovor_2 == "8":
            tocke += 1
    return tocke


print("Naloga 1")
print(ugibanje(4))

print("\nNaloga 2")
rezultat = mini_kviz("Pariz", "8")
print(f"V kvizu si dobil {rezultat} tocki.")

print("\nNaloga 3")
moznosti = ["Python", "Scratch", "HTML"]
print(f"Nakljucno izbran predmet: {random.choice(moznosti)}")