"""Resitve domace naloge - 09 While delavnica."""

print("Naloga 1")
kliki = [1, 1, 1, 1, 1]
skupaj_klikov = 0
indeks = 0
while indeks < len(kliki):
    skupaj_klikov += kliki[indeks]
    indeks += 1
print(f"Skupaj klikov: {skupaj_klikov}")

print("\nNaloga 2")
minute_vaje = [10, 15, 20]
skupaj_minut = 0
indeks = 0
while indeks < len(minute_vaje):
    skupaj_minut += minute_vaje[indeks]
    indeks += 1
print(f"Skupaj minut vaje: {skupaj_minut}")

print("\nNaloga 3")
vnos_cen = [3.0, 2.0, 4.5]
skupaj = 0
indeks = 0
while indeks < len(vnos_cen):
    skupaj += vnos_cen[indeks]
    indeks += 1
print(f"Koncni racun je {skupaj:.2f} EUR.")

print("\nNaloga 4")
print("Pri delavnici while je najbolj uporabno, da imam dober pogoj za ustavitev in stevec ali indeks.")