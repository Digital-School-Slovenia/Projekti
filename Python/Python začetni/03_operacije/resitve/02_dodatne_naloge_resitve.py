"""Rešitve dodatnih nalog – 03 – Osnovne operacije in računanje s programom."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

a = 18
b = 5

print("Naloga 1")
print(f"Vsota: {a + b}")
print(f"Razlika: {a - b}")
print(f"Produkt: {a * b}")
print(f"Kolicnik: {a / b}")

print("\nNaloga 2")
print(f"Ostanek pri deljenju {a} % {b} je {a % b}.")
print(f"Potenca {b} ** 2 je {b ** 2}.")

polmer = 7
obseg = 2 * 3.14 * polmer
print("\nNaloga 3")
print(f"Obseg kroga s polmerom {polmer} je priblizno {obseg:.2f}.")

ocene = [4, 5, 3, 5]
povprecje = sum(ocene) / len(ocene)
print("\nNaloga 4")
print(f"Povprecje ocen {ocene} je {povprecje:.2f}.")
