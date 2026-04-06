"""Rešitve dodatnih nalog – 12 – Seznami v praksi, `for` zanke in mini inventarji."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

nakupovalni_seznam = ["mleko", "kruh", "jabolka", "cokolada"]

print("Naloga 1")
for izdelek in nakupovalni_seznam:
    print(izdelek)

print("\nNaloga 2")
dolge_besede = [izdelek for izdelek in nakupovalni_seznam if len(izdelek) > 5]
print(dolge_besede)

cene = [1.2, 2.4, 3.8, 1.5]
print("\nNaloga 3")
print(f"Povprecna cena je {sum(cene) / len(cene):.2f} EUR.")
print(f"Najdrazji izdelek stane {max(cene):.2f} EUR.")

ocenjeni_casi = [15, 10, 20, 5]
print("\nNaloga 4")
print(f"Skupni cas opravkov je {sum(ocenjeni_casi)} minut.")
