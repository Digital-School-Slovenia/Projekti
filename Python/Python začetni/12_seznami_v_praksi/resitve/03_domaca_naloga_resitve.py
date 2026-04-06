"""Resitve domace naloge - 12 Seznami v praksi."""

naloge = ["domaca naloga", "ucenje", "sprehod", "vaja"]
print("Naloga 1")
print(f"Stevilo nalog: {len(naloge)}")

vrednosti = [7, 12, 3, 19, 8]
vecje_od_deset = [stevilo for stevilo in vrednosti if stevilo > 10]
print("\nNaloga 2")
print(vecje_od_deset)

poraba = [12, 15, 9, 11]
print("\nNaloga 3")
print(f"Povprecna poraba je {sum(poraba) / len(poraba):.2f}.")

print("\nNaloga 4")
print("Filtriranje v seznamih mi pomaga hitro poiskati elemente, ki ustrezajo pogoju.")