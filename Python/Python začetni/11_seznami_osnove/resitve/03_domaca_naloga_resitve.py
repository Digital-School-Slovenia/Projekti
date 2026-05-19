"""Rešitve domače naloge – 11 – Seznami – osnove in izpis z zankami."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

ucenci = ["Ana", "Bor", "Cene", "Dora"]
print("Naloga 1")
print(f"Prvi ucenec: {ucenci[0]}")
print(f"Zadnji ucenec: {ucenci[-1]}")

ocene = [5, 4, 4, 3]
print("\nNaloga 2")
print(f"Povprecje ocen je {sum(ocene) / len(ocene):.2f}.")

ocene.append(5)
print("\nNaloga 3")
print(f"Posodobljen seznam ocen: {ocene}")

print("\nNaloga 4")
print("Pri seznamih si moram zapomniti, da se indeksi zacnejo z 0.")
