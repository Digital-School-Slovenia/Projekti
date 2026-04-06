"""Rešitve dodatnih nalog – 13 – Nizi in oblikovanje izpisa."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

beseda = "programiranje"

print("Naloga 1")
print(f"Dolzina: {len(beseda)}")
print(f"Prva crka: {beseda[0]}")
print(f"Zadnja crka: {beseda[-1]}")

print("\nNaloga 2")
print(beseda.upper())
print(beseda.lower())

print("\nNaloga 3")
print(f"Prve 4 crke: {beseda[:4]}")
print(f"Zadnje 4 crke: {beseda[-4:]}")

samoglasniki = "aeiou"
stevec = sum(1 for znak in beseda if znak in samoglasniki)
print("\nNaloga 4")
print(f"Beseda vsebuje {stevec} samoglasnikov.")
