"""Rešitve dodatnih nalog – 02 – Spremenljivke in poimenovanje podatkov."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

cena_karte = 4.20
stevilo_kart = 5
skupna_cena = cena_karte * stevilo_kart
print("Naloga 1")
print(f"Za {stevilo_kart} kart placamo {skupna_cena:.2f} EUR.")

leta = 15
dni_priblizno = leta * 365
print("\nNaloga 2")
print(f"Oseba, stara {leta} let, je priblizno zivela {dni_priblizno} dni.")

sirina = 6
visina = 4
ploscina = sirina * visina
print("\nNaloga 3")
print(f"Pravokotnik velikosti {sirina} x {visina} ima ploscino {ploscina}.")

knjige_na_mesec = 3
meseci = 12
knjige_na_leto = knjige_na_mesec * meseci
print("\nNaloga 4")
print(f"Ce preberes {knjige_na_mesec} knjige na mesec, jih v letu preberes {knjige_na_leto}.")
