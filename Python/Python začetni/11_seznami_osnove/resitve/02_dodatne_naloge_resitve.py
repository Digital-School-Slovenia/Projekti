"""Rešitve dodatnih nalog – 11 – Seznami – osnove in izpis z zankami."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

predmeti = ["matematika", "slovenscina", "anglescina", "informatika"]

print("Naloga 1")
print(f"Prvi predmet: {predmeti[0]}")
print(f"Zadnji predmet: {predmeti[-1]}")

print("\nNaloga 2")
for predmet in predmeti:
    print(predmet)

ocene = [4, 5, 3, 5]
print("\nNaloga 3")
print(f"Vsota ocen: {sum(ocene)}")
print(f"Najvisja ocena: {max(ocene)}")
print(f"Najmanjsa ocena: {min(ocene)}")

predmeti.append("fizika")
predmeti.remove("slovenscina")
print("\nNaloga 4")
print(predmeti)
