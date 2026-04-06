"""Rešitve dodatnih nalog – 05 – Pogoji `if` – osnove odločanja."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

def polnoleten(starost):
    if starost >= 18:
        return "Oseba je polnoletna."
    return "Oseba se ni polnoletna."


def temperatura_opozorilo(temperatura):
    if temperatura > 30:
        return "Dan je zelo vroc."
    if temperatura < 0:
        return "Dan je leden."
    return "Temperatura je zmerna."


def je_sodo(stevilo):
    if stevilo % 2 == 0:
        return True
    return False


print("Naloga 1")
print(polnoleten(17))

print("\nNaloga 2")
print(temperatura_opozorilo(32))

print("\nNaloga 3")
print(f"Stevilo 14 je sodo: {je_sodo(14)}")

geslo = "python123"
vnos = "python123"
print("\nNaloga 4")
if vnos == geslo:
    print("Geslo je pravilno.")
else:
    print("Geslo ni pravilno.")
