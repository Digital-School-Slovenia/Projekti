"""Rešitve domače naloge – 03 – Osnovne operacije in računanje s programom."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

x = 25
y = 6

print("Naloga 1")
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")

minute = 137
ure = minute // 60
ostanek_minut = minute % 60
print("\nNaloga 2")
print(f"{minute} minut je {ure} ur in {ostanek_minut} minut.")

dolzina = 9
sirina = 4
ploscina = dolzina * sirina
print("\nNaloga 3")
print(f"Ploscina sobe je {ploscina} kvadratnih metrov.")

razmislek = "Pri operacijah moram paziti, kdaj uporabim navadno deljenje in kdaj celo stevilsko deljenje."
print("\nNaloga 4")
print(razmislek)
