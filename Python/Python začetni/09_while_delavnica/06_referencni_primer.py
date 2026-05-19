# Referenčni primer – 09 While delavnica
# Seštej cene petih izdelkov.

racun = 0.0
st_izdelkov = 0

while st_izdelkov < 5:
    cena_izdelka = float(input("Cena izdelka: "))
    racun = racun + cena_izdelka
    st_izdelkov = st_izdelkov + 1

print(f"Račun je bil: {racun:.2f} €")
